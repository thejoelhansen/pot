commands = {
    "docker test": {
        "arguments": "{arg1}",
        "body": 'docker run --rm busybox echo "{arg1}"',
        "help": "Docker hello world test.",
        "usage": (
            f"{'Usage:':<18} docker command <pattern>\n"
            f"{'Example:':<18} docker command containername"
        ),
        "runner": "shell"
    },
    "docker test2": {
        "arguments": "{arg2}",
        "body": 'docker run --rm busybox echo "{arg2}"',
        "help": "Another docker command.",
        "usage": (
            f"{'Usage:':<18} docker command <pattern>\n"
            f"{'Example:':<18} docker command containername"
        ), 
        "runner": "shell"
    }
}
