from .base import Base as BaseClass

class NIPA(BaseClass):
    """
    NIPA tables with options.
    """
    tableName = "NIPA"

    def __init__(self, api_key):
        super().__init__(self.tableName, api_key)
    

class GDPByIndustry(BaseClass):
    """
    Estimates of value added, gross output, intermediate inputs, KLEMS, and employment statistics by industry
    """

    tableName = "GDPByIndustry"

    def __init__(self, api_key):
        super().__init__(self.tableName, api_key)


class Regional(BaseClass):
    """
    Detailed income and employment statistics by state, county, and metropolitan area. 
    Detailed GDP statistics by state and metropolitan statistical area. 
    Price parities statistics by state and MSA.
    """

    tableName = "Regional"

    def __init__(self, api_key):
        super().__init__(self.tableName, api_key)


class UnderlyingGDPbyIndustry(BaseClass):
    """
    Underlying Detail estimates of value added, gross output, and 
    intermediate inputs by industry.
    """

    tableName ="UnderlyingGDPbyIndustry"

    def __init__(self, api_key):
        super().__init__(self.tableName, api_key)


class InputOutput(BaseClass):
    """
    Make and use tables, direct requirements, and total requirements statistics.    
    """

    tableName = "InputOutput"

    def __init__(self, api_key):
        super().__init__(self.tableName, api_key)


class NIUnderlyingDetail(BaseClass):
    """
    NI Underlying Detail tables with options.
    """

    tableName = "NIUnderlyingDetail"

    def __init__(self, api_key):
        super().__init__(self.tableName, api_key)


class FixedAssets(BaseClass):
    """
    Fixed Assets tables with options
    """

    tableName = "FixedAssets"

    def __init__(self, api_key):
        super().__init__(self.tableName, api_key)


class ITA(BaseClass):
    """
    International Transactions dataset by indicator, area or country, frequency, and year
    """

    tableName = "ITA"

    def __init__(self, api_key):
        super().__init__(self.tableName, api_key)


class IntlServTrade(BaseClass):
    """
    International Services Trade dataset by type of service, trade direction, affiliation, area or country, and year
    """

    tableName = "IntlServTrade"

    def __init__(self, api_key):
        super().__init__(self.tableName, api_key)


class IIP(BaseClass):
    """
    International Investment Position dataset by type of investment, component, frequency, and year
    """

    tableName = "IIP"

    def __init__(self, api_key):
        super().__init__(self.tableName, api_key)


class MNE(BaseClass):
    """
    Direct Investment by direction of investment, series, classification, year, country, and industry; and activities of Multinational Enterprises (MNE) by direction of investment, ownership, bank/non-bank, series, classification, year, country, industry, and state.
    """

    tableName = "MNE"

    def __init__(self, api_key):
        super().__init__(self.tableName, api_key)