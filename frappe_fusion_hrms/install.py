from frappe_fusion_hrms.setup import after_install as setup
import click

def after_install():
	try:
		print("Setting up Frappe Fusion Hrms...")
		setup()

		click.secho("Thank you for installing Frappe Fusion Hrms!", fg="green")

	except Exception as e:
		BUG_REPORT_EMAIL = "mohammadsami.ansari@fusionsofttech.co.in"
		click.secho(
			"Installation for Frappe Fusion Hrms app failed due to an error."
			" Please try re-installing the app or"
			f" report the issue on {BUG_REPORT_EMAIL} if not resolved.",
			fg="bright_red",
		)
		raise e