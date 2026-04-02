command = {
    "git search": {
        "arguments": "{pattern}",
        "body": 'git log -G"{pattern}" --oneline --patch',
        "help": "Search git history for a line matching the given pattern.",
        "usage": 'pot git search "<text>".',
        "runner": "shell"
    }
}
