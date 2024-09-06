class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []    # (content, identifier)
        digit_logs = []
        
        for log in logs:
            i = 0
            while log[i] != ' ':
                i += 1
                content, identifier = log[i + 1:], log[:i]

            if '0' <= content[0] <= '9':    # is a digit
                digit_logs.append(log)
            else:
                letter_logs.append((content, identifier))

        # print(letter_logs)
        # sort letter_logs and append digit_logs
        letter_logs.sort(key=lambda x:(x[0], x[1]))
        res = [' '.join([identifier, content]) for content, identifier in letter_logs]
        return res + digit_logs