"""

Written by: Jack Lee                                                   
Time: 2021/9/11 17:09                                                  

Function:   
                                            
"""
from django_filters import rest_framework as drf_filters

from .models import Group, NFTContract


class GroupFilter(drf_filters.FilterSet):
    class Meta:
        model = Group

        fields = ['address']

    # 跨表查询
    address = drf_filters.CharFilter(field_name="nft__address", lookup_expr='iexact')
    # address = NFTContractFilter
