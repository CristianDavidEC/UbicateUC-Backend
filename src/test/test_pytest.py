from handlers.SitesHandlers import get_site


def test_find_by_id_ok():
    site = get_site('629e5891e59df4c1b8996ec8')
    assert site['nombre'] == 'Baño B3'
    assert site['tipo'] == 'Baño'


def test_find_by_id_not_found():
    site = get_site('629a5891c58df4c1b8996ec8')
    assert site is None


'''def test_filter_name_ok():
    sites = get_filter_sites('Sala')
    assert len(sites) == 2'''
