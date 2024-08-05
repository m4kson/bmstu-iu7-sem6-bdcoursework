DROP TRIGGER update_service_request_status_trigger ON servicereports;
DROP TRIGGER update_line_status_trigger ON servicerequests;
DROP TRIGGER update_assemblyline_trigger ON servicereports;

CREATE OR REPLACE FUNCTION update_service_request_status()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE servicerequests
    SET status = 'закрыта'
    WHERE id = NEW.requestid;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;


CREATE TRIGGER update_service_request_status_trigger
AFTER INSERT ON servicereports
FOR EACH ROW
EXECUTE FUNCTION update_service_request_status();



CREATE OR REPLACE FUNCTION update_line_status()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE assemblylines
    SET status = 'на обслуживании'
    WHERE  id = NEW.lineid;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_line_status_trigger
AFTER INSERT ON servicerequests
FOR EACH ROW
EXECUTE FUNCTION update_line_status();



CREATE OR REPLACE FUNCTION update_assemblyline_after_report()
RETURNS TRIGGER AS $$
DECLARE
    downtime_hours INTEGER;
    next_inspection_date DATE;
BEGIN
    downtime_hours := EXTRACT(EPOCH FROM (NEW.closedate - (SELECT requestdate FROM servicerequests WHERE id = NEW.requestid))) / 3600;

    UPDATE assemblylines
    SET downtime = downtime + downtime_hours,
        status = 'работает'
    WHERE id = NEW.lineid;

    IF (SELECT type FROM servicerequests WHERE id = NEW.requestid) = 'техосмотр' THEN
        UPDATE assemblylines
        SET lastinspectiondate = NEW.closedate,
            nextinspectiondate = NEW.closedate + interval '1 month' * (12 / (SELECT inspectionsamountperyear FROM assemblylines WHERE id = NEW.lineid))
        WHERE id = NEW.lineid;
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_assemblyline_trigger
AFTER INSERT ON servicereports
FOR EACH ROW
EXECUTE FUNCTION update_assemblyline_after_report();


