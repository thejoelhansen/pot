commands = {
    "notify discord": {
        "arguments": "{arg1}",
        "body": "bash -c 'source ~/.pot/.env && curl -H \"Content-Type: application/json\" -d \"{{\\\"content\\\": \\\"{arg1}\\\"}}\" $POT_DISCORD_WEBHOOK'",
        "help": "Send a message to Discord using the configured webhook.",
        "usage": "Usage: pot notify discord <message>",
        "runner": "shell"
    }
}

