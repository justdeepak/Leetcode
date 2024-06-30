# https://leetcode.com/problems/unique-email-addresses/

from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniqueEmails = set()

        for email in emails:

            username, domain = email.split("@")

            username = username.split("+")[0]
            username = username.replace(".", "")

            uniqueEmails.add(username + "@" + domain)

        return len(uniqueEmails)
