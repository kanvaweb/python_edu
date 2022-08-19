import string

formatter = string.Formatter()
print(formatter.format('{userLog}', userLog = 'Admin'))
print(formatter.format('{} {userName}', userName = 'Admin'))
print(formatter.format(f'{userRights}', userRights = 'RIGHTS'))


t=string.Template('$userName has the rights to $userRights in the $appName')

str = t.substitute(userName = "adm",
                userRights="full",
                appName="Prog")
print(str)
print(str)