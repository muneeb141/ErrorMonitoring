# ERPNext Error Monitor

A custom ERPNext app that monitors error logs and sends notifications to Telegram users through n8n automation.

## Features

- Real-time error monitoring for ERPNext
- Telegram notifications for system errors
- Configurable monitoring for specific DocTypes
- Support for multiple Telegram users
- Customizable error message format
- Simple setup and configuration

## Prerequisites

Before installing this app, ensure you have:

1. ERPNext (Version 14 or later)
2. Python 3.7+
3. n8n installed and running
4. Telegram account and bot setup

## Installation

1. From your bench directory:
```bash
bench get-app error_monitoring https://github.com/YOUR_USERNAME/error_monitoring
bench install-app error_monitoring
```

2. After installation, run migrations:
```bash
bench migrate
```

## Setup Instructions

### 1. Telegram Bot Setup

1. Create a Telegram bot:
   - Open Telegram and search for @BotFather
   - Send `/newbot` command
   - Follow instructions to create your bot
   - Save the bot token provided

2. Get Chat IDs:
   - Add @RawDataBot to your group or
   - Send message to your bot and check: `https://api.telegram.org/botYOUR_BOT_TOKEN/getUpdates`
   - Note down the chat IDs for configuration

### 2. n8n Setup

1. Start n8n:
```bash
n8n start
```

2. Create new workflow:
   - Access n8n interface (default: http://localhost:5678)
   - Create new workflow
   - Add Webhook node (trigger)
   - Add Split In Batches node
   - Add Telegram node
   - Configure nodes as shown in screenshots below

3. Configure Telegram node:
   - Add your bot token
   - Use dynamic chat ID: `{{$json["chat_id"]}}`
   - Save and activate workflow
   - Copy webhook URL

### 3. ERPNext Configuration

1. Go to Error Monitor Settings:
   - Add n8n webhook URL
   - Enable monitoring
   - Add Telegram users and chat IDs
   - Configure DocTypes to monitor

2. Test the setup:
```python
# In bench console
error_log = frappe.new_doc('Error Log')
error_log.error_type = "Test Error"
error_log.error_message = "Test Message"
error_log.insert(ignore_permissions=True)
```

## Configuration Options

### Error Monitor Settings

| Field | Description |
|-------|-------------|
| n8n Webhook URL | URL from n8n workflow |
| Enable Monitoring | Toggle monitoring on/off |
| Monitor All DocTypes | Monitor errors from all DocTypes |
| Telegram Users | List of users to notify |
| Monitored DocTypes | Specific DocTypes to monitor |

### Telegram User Settings

| Field | Description |
|-------|-------------|
| User Name | Identifier for the user |
| Chat ID | Telegram chat ID |
| Active | Toggle notifications for user |

## Troubleshooting

1. **No notifications received:**
   - Check if n8n is running
   - Verify webhook URL in settings
   - Confirm Telegram chat IDs are correct
   - Check Error Monitor Settings are enabled

2. **n8n webhook errors:**
   - Ensure n8n is running
   - Check workflow is activated
   - Verify webhook URL format

3. **ERPNext errors:**
   - Check system logs: `bench --site your_site_name show-log`
   - Verify app is installed: `bench list-apps`

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Support

For support:
- Open an issue on GitHub
- Contact: muneebmohammed141@gmail.com

## Screenshots

![image](https://github.com/user-attachments/assets/379327a6-acb9-4002-b686-55daa8fec620)


## Version History

- 1.0.0
  - Initial Release
  - Basic error monitoring
  - Telegram integration
