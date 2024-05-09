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

