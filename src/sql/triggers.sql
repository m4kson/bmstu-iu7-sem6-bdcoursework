-- trigger2 меняет статус заявки на обслуживание после добавления записи в таблицу отчетов об обслуживании
CREATE OR REPLACE FUNCTION update_service_request_status()
RETURNS TRIGGER AS $$
BEGIN
    -- Обновляем статус заявки на "завершена" после добавления отчета об обслуживании
    UPDATE servicerequests
    SET status = 'завершена'
    WHERE id = NEW.requestid;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Создаем AFTER триггер для таблицы servicereports
CREATE TRIGGER update_service_request_status_trigger
AFTER INSERT ON servicereports
FOR EACH ROW
EXECUTE FUNCTION update_service_request_status();


--trigger4 меняет статус производственной линии при создании заявки на ее техобслуживание
CREATE OR REPLACE FUNCTION update_line_status()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE assemblylines
    SET status = 'на обслуживании'
    WHERE  id = NEW.lineid;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Создаем AFTER триггер для таблицы servicerequests
CREATE TRIGGER update_line_status_trigger
AFTER INSERT ON servicerequests
FOR EACH ROW
EXECUTE FUNCTION update_line_status();



-- trigger3 обновляет значение поля DownTime и status а также в случае если было проведено техобслуживание меняет знаяения полей LastInspectionDate и NextInspectiondate
CREATE OR REPLACE FUNCTION update_assemblyline_after_report()
RETURNS TRIGGER AS $$
DECLARE
    downtime_hours INTEGER;
    next_inspection_date DATE;
BEGIN
    -- Вычисляем количество часов с момента открытия заявки до публикации отчета об обслуживании
    downtime_hours := EXTRACT(EPOCH FROM (NEW.closedate - (SELECT requestdate FROM servicerequests WHERE id = NEW.requestid))) / 3600;

    -- Обновляем поле DownTime в соответствии с вычисленным значением
    UPDATE assemblylines
    SET downtime = downtime + downtime_hours,
        status = 'работает'
    WHERE id = NEW.lineid;

    -- Если тип заявки на обслуживание был "техосмотр"
    IF (SELECT type FROM servicerequests WHERE id = NEW.requestid) = 'техосмотр' THEN
        -- Изменяем значение поля LastInspectionDate на дату закрытия отчета об обслуживании
        UPDATE assemblylines
        SET lastinspectiondate = NEW.closedate,
            -- Прибавляем к полю NextInspectionDate количество месяцев, вычисленное делением 12 на InspectionsAmountPerYear
            nextinspectiondate = NEW.closedate + interval '1 month' * (12 / (SELECT inspectionsamountperyear FROM assemblylines WHERE id = NEW.lineid))
        WHERE id = NEW.lineid;
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Создаем AFTER триггер для таблицы servicereports
CREATE TRIGGER update_assemblyline_trigger
AFTER INSERT ON servicereports
FOR EACH ROW
EXECUTE FUNCTION update_assemblyline_after_report();


