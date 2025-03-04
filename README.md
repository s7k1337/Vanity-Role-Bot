# 🎀 Vanity-Role-Bot

This is a Discord bot that automatically assigns and removes roles to members based on their custom status. When a member sets a specific keyword in their status (defined in the bot's configuration), the bot assigns them a role, and when they remove it, the bot removes the role.

## Features:
- Assigns a specific role to members based on their custom activity status.
- Removes the role if the member's status no longer matches the defined keyword.
- Sends log messages in a specific channel with embed notifications about role changes.

## Requirements:
- Python 3.6+
- `discord.py` library

## Setup Instructions:

### 1. Install Python and Dependencies:
Make sure Python 3.6 or above is installed. If not, you can download and install it from [here](https://www.python.org/downloads/).

Install the necessary Python package using pip:

```bash
pip install discord.py
```

### 2. Set up `config.json`:
Create a `config.json` file in the same directory as your bot. Below is an example configuration:

```json
{
  "TOKEN": "YOUR_BOT_TOKEN",
  "GUILD_ID": "YOUR_SERVER_ID",
  "SUPPORTER_ROLE_ID": "YOUR_ROLE_ID",
  "LOG_CHANNEL_ID": "YOUR_LOG_CHANNEL_ID",
  "KEYWORDS": ["custom_status1", "custom_status2", "custom_status3", "custom_status4"]
}
```

- Replace `"YOUR_BOT_TOKEN"` with your bot's token (which you can get from the [Discord Developer Portal](https://discord.com/developers/applications)).
- Replace `"YOUR_SERVER_ID"`, `"YOUR_ROLE_ID"`, and `"YOUR_LOG_CHANNEL_ID"` with the corresponding IDs for your server, role, and log channel.
- The `"KEYWORDS"` array contains the keywords the bot will look for in a member's status to assign the role.

### 3. Add the Bot to Your Server:
1. Go to the [Discord Developer Portal](https://discord.com/developers/applications).
2. Select your bot application and navigate to the **OAuth2** tab.
3. Under **OAuth2 URL Generator**, select `bot` as a scope and grant the necessary permissions (like `Manage Roles` and `Read Messages`).
4. Copy the generated URL and use it to invite the bot to your server.

### 4. Run the Bot:
Once everything is set up, simply run the bot:

```bash
python main.py
```

### 5. Logs:
The bot will send embed logs to the specified log channel when a role is assigned or removed.

## Customization:
- You can change the **embed colors** and **author icon** within the `main.py` file.
- You can also modify the **embed description** text directly in the `main.py`.

## License:
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support:
If you encounter any issues or need help, feel free to open an issue on this repository.
