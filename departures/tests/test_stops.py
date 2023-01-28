from departures.stops import get_stops


def test_get_stops():
    stops = get_stops("Düsseldorf", "Heinrich-Heine-Allee U")

    assert "U71" in stops["servingLines"]["lines"][0]["mode"]["number"]
    assert "20018262" in stops["servingLines"]["lines"][0]["mode"]["destID"]
    assert (
        "D-Benrath Btf"
        in stops["servingLines"]["lines"][0]["mode"]["destination"]
    )
