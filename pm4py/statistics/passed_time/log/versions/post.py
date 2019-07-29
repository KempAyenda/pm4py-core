from pm4py.algo.discovery.dfg import factory as dfg_factory


def apply(log, activity, parameters=None):
    """
    Gets the time passed to each succeeding activity

    Parameters
    -------------
    log
        Log
    activity
        Activity that we are considering
    parameters
        Possible parameters of the algorithm

    Returns
    -------------
    list_aggr_times
        List of aggregates times from the given activity to each succeeding activity
    """
    if parameters is None:
        parameters = {}

    dfg = dfg_factory.apply(log, variant="performance", parameters=parameters)

    ret = []

    for entry in dfg.keys():
        if entry[0] == activity:
            ret.append([entry[1], float(dfg[entry])])

    return ret