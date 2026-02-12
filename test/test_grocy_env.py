import pytest

from grocy.grocy import Grocy


class TestGrocyEnvConfig:
    def test_loads_base_url_and_api_key_from_env(self, monkeypatch):
        monkeypatch.setenv("GROCY_BASE_URL", "http://grocy-env")
        monkeypatch.setenv("GROCY_API_KEY", "env-api-key")

        client = Grocy()

        assert client._api_client._base_url == "http://grocy-env:9192/api/"
        assert client._api_client._headers["GROCY-API-KEY"] == "env-api-key"

    def test_explicit_constructor_values_override_env(self, monkeypatch):
        monkeypatch.setenv("GROCY_BASE_URL", "http://grocy-env")
        monkeypatch.setenv("GROCY_API_KEY", "env-api-key")

        client = Grocy("http://grocy-arg", "arg-api-key")

        assert client._api_client._base_url == "http://grocy-arg:9192/api/"
        assert client._api_client._headers["GROCY-API-KEY"] == "arg-api-key"

    def test_raises_when_base_url_missing(self, monkeypatch):
        monkeypatch.delenv("GROCY_BASE_URL", raising=False)
        monkeypatch.setenv("GROCY_API_KEY", "env-api-key")

        with pytest.raises(ValueError, match="GROCY_BASE_URL"):
            Grocy()

    def test_raises_when_api_key_missing(self, monkeypatch):
        monkeypatch.setenv("GROCY_BASE_URL", "http://grocy-env")
        monkeypatch.delenv("GROCY_API_KEY", raising=False)

        with pytest.raises(ValueError, match="GROCY_API_KEY"):
            Grocy()
