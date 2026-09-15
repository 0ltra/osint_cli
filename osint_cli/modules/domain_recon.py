import dns.resolver


def get_dns_records(domain):
    record_types = ["A", "MX", "TXT"]
    results = {}

    for rtype in record_types:
        try:
            answers = dns.resolver.resolve(domain, rtype)
            results[rtype] = []
            for rdata in answers:
                results[rtype].append(str(rdata))

        except dns.resolver.NXDOMAIN:
            # TODO: what should happen here? domain doesn't exist at all —
            # arguably you don't even need to keep trying other record types
            pass
        except dns.resolver.NoAnswer:
            # TODO: domain exists, just no records of this type — skip it
            pass

    return results
