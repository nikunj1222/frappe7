import frappe

def execute():
	frappe.reload_doctype("Scheduler Log")

	from frappe.core.doctype.scheduler_log.scheduler_log import set_old_logs_as_seen
	set_old_logs_as_seen()
