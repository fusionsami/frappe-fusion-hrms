from frappe_fusion_hrms.setup import before_uninstall as remove_custom_fields
import click

def before_uninstall():
	try:
		print("Removing customizations created by the Frappe Fusion Hrms...")
		remove_custom_fields()

	except Exception as e:
		BUG_REPORT_EMAIL = "mohammadsami.ansari@fusionsofttech.co.in"
		click.secho(
			"Removing Customizations for Frappe Fusion Hrms failed due to an error."
			" Please try again or"
			f" report the issue on {BUG_REPORT_EMAIL} if not resolved.",
			fg="bright_red",
		)
		raise e
	
	click.secho("Frappe Fusion Hrms app customizations have been removed successfully...", fg="green")
    
    