def createResultObj(newdf):
    newdf.columns = ['IMPROVE', 'DOMAIN', 'SUBDOMAIN', 'SENTIMENT']

    domains = {
        'chartTitle': 'Overall Results across all Domains',
        'labels': [],
        'positive': [],
        'negative': [],
        'both': []
    }

    assessment = {
        'chartTitle': 'Results for Comments on Assessment',
        'labels': [],
        'positive': [],
        'negative': [],
        'both': []
    }

    course = {
        'chartTitle': 'Results for Comments on Course',
        'labels': [],
        'positive': [],
        'negative': [],
        'both': []
    }

    outcomes = {
        'chartTitle': 'Results for Comments on Outcomes',
        'labels': [],
        'positive': [],
        'negative': [],
        'both': []
    }

    staff = {
        'chartTitle': 'Results for Comments on Staff',
        'labels': [],
        'positive': [],
        'negative': [],
        'both': []
    }

    support = {
        'chartTitle': 'Results for Comments on Support',
        'labels': [],
        'positive': [],
        'negative': [],
        'both': []
    }

    g1 = newdf.groupby(["DOMAIN", "SUBDOMAIN", "SENTIMENT"]).count().reset_index()
    domnames = g1.DOMAIN.unique()

    for dom in domnames:
        dpcount = 0
        dncount = 0
        domains['labels'].append(dom)
        sdomnames = g1.query('DOMAIN == @dom').SUBDOMAIN.unique()
        for sdom in sdomnames:
            tp = g1.query('DOMAIN == @dom and SUBDOMAIN == @sdom and SENTIMENT == "positive"').IMPROVE.sum()
            tn = g1.query('DOMAIN == @dom and SUBDOMAIN == @sdom and SENTIMENT == "negative"').IMPROVE.sum()
            dpcount += tp
            dncount += tn
            if dom == "ASSESSMENT":
                assessment['labels'].append(sdom)
                assessment['positive'].append(int(tp))
                assessment['negative'].append(int(tn))
                assessment['both'].append(int(tn)+int(tp))
            elif dom == "COURSE/UNIT DESIGN":
                course['labels'].append(sdom)
                course['positive'].append(int(tp))
                course['negative'].append(int(tn))
                course['both'].append(int(tn) + int(tp))
            elif dom == "OUTCOMES":
                outcomes['labels'].append(sdom)
                outcomes['positive'].append(int(tp))
                outcomes['negative'].append(int(tn))
                outcomes['both'].append(int(tn) + int(tp))
            elif dom == "STAFF":
                staff['labels'].append(sdom)
                staff['positive'].append(int(tp))
                staff['negative'].append(int(tn))
                staff['both'].append(int(tn) + int(tp))
            elif dom == "SUPPORT":
                support['labels'].append(sdom)
                support['positive'].append(int(tp))
                support['negative'].append(int(tn))
                support['both'].append(int(tn) + int(tp))
        domains['positive'].append(int(dpcount))
        domains['negative'].append(int(dncount))
        domains['both'].append(int(dpcount) + int(dncount))
    return domains, assessment, course, outcomes, staff, support
