class Solution:
    def subdomainVisits(self, cpdomains: list[str]) -> list[str]:
        counts = {}

        for cpdomain in cpdomains:
            visits, domain = cpdomain.split()
            visits = int(visits)

            parts = domain.split(".")

            for i in range(len(parts)):
                subdomain = ".".join(parts[i:])

                counts[subdomain] = counts.get(subdomain, 0) + visits

        result = []

        for domain, visits in counts.items():
            result.append(str(visits) + " " + domain)

        return result