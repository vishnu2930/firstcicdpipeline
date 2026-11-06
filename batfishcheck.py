"""Script used to test network configurations with Batfish."""

import os

from pybatfish.client.session import Session
from pybatfish.client.asserts import (
    assert_no_duplicate_router_ids,
    assert_no_incompatible_bgp_sessions,
    assert_no_incompatible_ospf_sessions,
    assert_no_unestablished_bgp_sessions,
    assert_no_undefined_references,
)

from rich.console import Console

console = Console(color_system="truecolor")


def test_duplicate_rtr_ids(snap, bf):
    """Test for duplicate router IDs."""
    console.print("\n[bold yellow]Testing for duplicate router IDs[/bold yellow]")

    assert_no_duplicate_router_ids(
        snapshot=snap,
        protocols=["ospf", "bgp"],
        session=bf,
    )

    console.print("[bold green]No duplicate router IDs found[/bold green]")


def test_bgp_compatibility(snap, bf):
    """Test for incompatible BGP sessions."""
    console.print("\n[bold yellow]Testing for incompatible BGP sessions[/bold yellow]")

    assert_no_incompatible_bgp_sessions(
        snapshot=snap,
        session=bf,
    )

    console.print("[bold green]All BGP sessions compatible![/bold green]")


def test_ospf_compatibility(snap, bf):
    """Test for incompatible OSPF sessions."""
    console.print("\n[bold yellow]Testing for incompatible OSPF sessions[/bold yellow]")

    assert_no_incompatible_ospf_sessions(
        snapshot=snap,
        session=bf,
    )

    console.print("[bold green]All OSPF sessions compatible![/bold green]")


def test_bgp_unestablished(snap, bf):
    """Test for BGP sessions that are not established."""
    console.print("\n[bold yellow]Testing for unestablished BGP sessions[/bold yellow]")

    assert_no_unestablished_bgp_sessions(
        snapshot=snap,
        session=bf,
    )

    console.print("[bold green]All BGP sessions are established![/bold green]")


def test_undefined_references(snap, bf):
    """Test for undefined references."""
    console.print("\n[bold yellow]Testing for undefined references[/bold yellow]")

    assert_no_undefined_references(
        snapshot=snap,
        session=bf,
    )

    console.print("[bold green]No undefined references found![/bold green]")


def main():
    """Connect to Batfish, initialize snapshot, and run tests."""

    NETWORK_NAME = "CICD_DEMO"
    SNAPSHOT_NAME = "snapshot00"
    SNAPSHOT_DIR = "./snapshots/snapshot00"

    # Set BATFISH_HOST to the reachable Batfish server hostname/IP.
    BATFISH_HOST = "localhost"

    console.print("[bold cyan]Connecting to Batfish...[/bold cyan]")

    bf = Session(host=BATFISH_HOST)

    # Create or select the Batfish network.
    bf.set_network(NETWORK_NAME)

    # Initialize the snapshot.
    console.print("[bold cyan]Initializing Batfish snapshot...[/bold cyan]")

    snap = bf.init_snapshot(
        SNAPSHOT_DIR,
        name=SNAPSHOT_NAME,
        overwrite=True,
    )

    console.print(f"[bold green]Snapshot initialized: {snap}[/bold green]")

    # Run network validation tests.
    test_duplicate_rtr_ids(snap, bf)
    test_bgp_compatibility(snap, bf)
    test_ospf_compatibility(snap, bf)
    test_bgp_unestablished(snap, bf)
    test_undefined_references(snap, bf)

    console.print(
        "\n[bold green]All Batfish network validation tests passed![/bold green]"
    )


if __name__ == "__main__":
    main()
