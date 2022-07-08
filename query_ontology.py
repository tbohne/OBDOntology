import rdflib

ONTOLOGY_FILE = "obd_ontology.owl"
ONTOLOGY_PREFIX = "<http://www.semanticweb.org/tbohne-p15s/ontologies/2022/6/diag_ontology#>"


def complete_ontology_entry(entry):
    return ONTOLOGY_PREFIX.replace('#', '#' + entry)


def query_fault_causes_by_dtc(dtc, g):
    print("QUERY: fault causes for " + dtc)
    dtc_entry = complete_ontology_entry(dtc)
    represents_entry = complete_ontology_entry('represents')
    fault_cause_entry = complete_ontology_entry('FaultCause')
    has_cause_entry = complete_ontology_entry('hasCause')
    s = f"""
    SELECT ?cause WHERE {{
        {dtc_entry} {represents_entry} ?condition .
        ?cause a {fault_cause_entry} .
        ?condition {has_cause_entry} ?cause .
    }}
    """
    for row in g.query(s):
        print("--> ", str(row).split(ONTOLOGY_PREFIX.replace("<", "").replace(">", ""))[1].replace("'),)", ""))


if __name__ == '__main__':
    graph = rdflib.Graph()
    graph = graph.parse(ONTOLOGY_FILE, format='xml')
    query_fault_causes_by_dtc("P0138", graph)