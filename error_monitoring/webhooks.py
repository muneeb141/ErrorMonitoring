import frappe
import requests
import json
from typing import Dict, Any

def send_error_notification(doc, method):
    """Send error notification to n8n webhook"""
    try:
        settings = frappe.get_doc('Error Monitor Settings')
        
        if not settings.enabled:
            return

        # Check if we should monitor this doctype
        if not settings.monitor_all_doctypes:
            monitored_doctypes = [d.doctype_name for d in settings.monitored_doctypes if d.is_active]
            if doc.reference_doctype and doc.reference_doctype not in monitored_doctypes:
                return
        
        # Get active telegram users
        telegram_users = [user for user in settings.telegram_users if user.is_active]
        if not telegram_users:
            frappe.log_error('No active Telegram users configured', 'Error Monitor')
            return

        # Prepare error data
        error_data = {
            'error_type': doc.error_type,
            'error_name': doc.name,
            'error_message': doc.error_message,
            'error_description': doc.error_description,
            'reference_doctype': doc.reference_doctype or 'Not Specified',
            'reference_name': doc.reference_name or 'Not Specified',
            'timestamp': str(doc.creation),
            'site_name': frappe.local.site,
            'telegram_users': [{'chat_id': user.chat_id, 'user_name': user.user_name} 
                             for user in telegram_users]
        }
        
        # Send to n8n webhook
        response = requests.post(
            settings.n8n_webhook_url,
            json=error_data,
            headers={'Content-Type': 'application/json'}
        )
        response.raise_for_status()
        
        frappe.logger().info(f'Error notification sent to {len(telegram_users)} users for {doc.name}')
        
    except Exception as e:
        frappe.log_error(
            f'Failed to send error notification to n8n: {str(e)}',
            'Error Monitor Webhook'
        )