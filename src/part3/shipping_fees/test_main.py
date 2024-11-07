import pytest
from .main import calculate_shipping_fee


shipping_fee_s = 4.99
shipping_fee_s_half = 2.49
shipping_fee_m = 9.99
shipping_fee_m_half = 4.99
shipping_fee_l = 14.99
shipping_fee_l_half = 7.49


class TestShippingFees:

    class TestShippingFeesByPrice:
        @pytest.mark.parametrize(
            "total_price, total_weight, expected_shipping_fee",
            [
                (10, 0, shipping_fee_s),
                (10, 0.01, shipping_fee_s),
                (10, 0.98, shipping_fee_s),
                (10, 0.99, shipping_fee_s),
                (0, 0.5, shipping_fee_s),
                (0.01, 0.5, shipping_fee_s),
                (49.99, 0.5, shipping_fee_s),
                (50, 0.5, shipping_fee_s),
            ],
        )
        def test_calculate_shipping_fee_low_price_small_package(
            self, total_price, total_weight, expected_shipping_fee
        ):
            assert (
                calculate_shipping_fee(total_price, total_weight)
                == expected_shipping_fee
            )

        @pytest.mark.parametrize(
            "total_price, total_weight, expected_shipping_fee",
            [
                (70, 0, shipping_fee_s_half),
                (70, 0.01, shipping_fee_s_half),
                (70, 0.98, shipping_fee_s_half),
                (70, 0.99, shipping_fee_s_half),
                (50.01, 0.5, shipping_fee_s_half),
                (50.02, 0.5, shipping_fee_s_half),
                (100, 0.5, shipping_fee_s_half),
                (99.99, 0.5, shipping_fee_s_half),
            ],
        )
        def test_calculate_shipping_fee_medium_price_small_package(
            self, total_price, total_weight, expected_shipping_fee
        ):
            assert (
                calculate_shipping_fee(total_price, total_weight)
                == expected_shipping_fee
            )

        @pytest.mark.parametrize(
            "total_price, total_weight, expected_shipping_fee",
            [
                (150, 0, 0),
                (150, 0.01, 0),
                (150, 0.98, 0),
                (150, 0.99, 0),
                (100.01, 0.5, 0),
                (100.02, 0.5, 0),
                (20000, 0.5, 0),
            ],
        )
        def test_calculate_shipping_fee_high_price_small_package(
            self, total_price, total_weight, expected_shipping_fee
        ):
            assert (
                calculate_shipping_fee(total_price, total_weight)
                == expected_shipping_fee
            )

    class TestShippingFeesByWeight:
        @pytest.mark.parametrize(
            "total_price, total_weight, expected_shipping_fee",
            [
                (10, 0, shipping_fee_s),
                (10, 0.01, shipping_fee_s),
                (10, 0.98, shipping_fee_s),
                (10, 0.99, shipping_fee_s),
            ],
        )
        def test_calculate_shipping_fee_small_package(
            self, total_price, total_weight, expected_shipping_fee
        ):
            assert (
                calculate_shipping_fee(total_price, total_weight)
                == expected_shipping_fee
            )

        @pytest.mark.parametrize(
            "total_price, total_weight, expected_shipping_fee",
            [
                (10, 1, shipping_fee_m),
                (10, 1.01, shipping_fee_m),
                (10, 4.98, shipping_fee_m),
                (10, 4.99, shipping_fee_m),
            ],
        )
        def test_calculate_shipping_fee_medium_package(
            self, total_price, total_weight, expected_shipping_fee
        ):
            assert (
                calculate_shipping_fee(total_price, total_weight)
                == expected_shipping_fee
            )

        @pytest.mark.parametrize(
            "total_price, total_weight, expected_shipping_fee",
            [
                (10, 5, shipping_fee_l),
                (10, 5.01, shipping_fee_l),
                (10, 100, shipping_fee_l),
                (10, 1000, shipping_fee_l),
            ],
        )
        def test_calculate_shipping_fee_large_package(
            self, total_price, total_weight, expected_shipping_fee
        ):
            assert (
                calculate_shipping_fee(total_price, total_weight)
                == expected_shipping_fee
            )

    class TestShippingFeesExceptions:
        def test_calculate_shipping_fee_price_exception(self):
            with pytest.raises(
                ValueError, match="Total price must not be negative, got -1"
            ):
                calculate_shipping_fee(-1, 1)

        def test_calculate_shipping_fee_weight_exception(self):
            with pytest.raises(
                ValueError, match="Weight must not be negative, got -1"
            ):
                calculate_shipping_fee(1, -1)
