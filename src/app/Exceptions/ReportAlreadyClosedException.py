class ReportAlreadyClosedException(Exception):
    def __init__(self, report_id: int):
        self.report_id = report_id
        self.message = f"Service report with id {report_id} is already closed"
        super().__init__(self.message)