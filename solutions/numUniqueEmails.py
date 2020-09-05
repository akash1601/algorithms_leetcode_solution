class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        if not emails:
            return 0
        num = 0
        handled_emails = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0]
            local = local.replace('.','')
            handled_emails.add((local,domain))
        return len(handled_emails)
        