pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+=-])(?=.{8,})"
# ^ Matches the expression to its right, at the start of a string before it experiences a line break
# $ Matches the expression to its left, at the end of a string before it experiences a line break
# . Matches any character except newline
# a Matches exactly one character a
# xy Matches the string xy
# a|b Matches expression a or b. If a is matched first, b is left untried

                            #    another ex
pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+=-])(?=.{8,})"
#r  - raw string
# .: Matches any single character (except a newline).
# *: Matches zero or more of the preceding character or group.
# +: Matches one or more of the preceding character or group.
# ?: Matches zero or one of the preceding character or group.
# [ ]: Matches any character within the brackets.
# ^: Matches the start of a string.
# $: Matches the end of a string.
# \d: Matches any digit (equivalent to [0-9]).
# \w: Matches any word character (equivalent to [a-zA-Z0-9_]).
# \s: Matches any whitespace character (including space, tab, and newline).​


