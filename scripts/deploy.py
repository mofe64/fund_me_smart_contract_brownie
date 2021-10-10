from brownie import FundMe, network, config, MockV3Aggregator
from scripts.util import deploy_mocks, get_account, LOCAL_BLOCK_CHAIN_ENV


def deploy_fund_me():
    account = get_account()
    if network.show_active() not in LOCAL_BLOCK_CHAIN_ENV:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"contract deployed to {fund_me.address}")


def main():
    deploy_fund_me()
