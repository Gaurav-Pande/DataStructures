# https://leetcode.com/problems/unique-email-addresses/
class Solution(object):
	def numUniqueEmails(self, emails):
		"""
		:type emails: List[str]
		:rtype: int
		"""
		s = set()
		for email in emails:
			p = email.split("@")

			local, dns = p[0], p[1]
			# print(local,dns)
			if '.' in local:
				local = local.replace('.', '')
			# print(local)
			if '+' in local:
				s.add(str(local.split('+')[0]) + '@' + str(dns))
				continue

			s.add(str(local) + '@' + str(dns))

		# print(s)
		return len(s)


