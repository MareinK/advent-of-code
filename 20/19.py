import functools

(rules_str, messages_str) = open("19.txt").read().split("\n\n")
rules = dict(line.split(": ") for line in rules_str.splitlines())
messages = messages_str.splitlines()


@functools.lru_cache(maxsize=2 ** 32)
def match_rule(rule, message):
    if rule.startswith('"') and rule.endswith('"'):
        return message == rule.strip('"')
    if rule.isdigit():
        return match_rule(rules[rule], message)
    if " | " in rule:
        return any(match_rule(r, message) for r in rule.split(" | "))
    if " " in rule:
        first, rest = rule.split(" ", maxsplit=1)
        return any(
            match_rule(first, message[:i]) and match_rule(rest, message[i:])
            for i in range(len(message))
        )


# part 1
print(len([m for m in messages if match_rule("0", m)]))

# part 2
match_rule.cache_clear()
rules["8"] = "42 | 42 8"
rules["11"] = "42 31 | 42 11 31"
print(len([m for m in messages if match_rule("0", m)]))
