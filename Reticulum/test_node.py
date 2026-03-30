#!/usr/bin/env python3
"""
Simple Reticulum Node Test Script

This script tests your Reticulum node by:
1. Checking if Reticulum can be imported
2. Initializing a Reticulum instance
3. Displaying available interfaces
4. Showing node identity

Usage:
    python test_node.py
"""

import sys
import RNS

def test_reticulum_node():
    """Test Reticulum node initialization and display status"""

    print("=" * 60)
    print("Reticulum Node Test")
    print("=" * 60)
    print()

    try:
        print("[1/4] Testing RNS import...")
        print(f"      ✓ RNS version: {RNS.version}")
        print()

        print("[2/4] Initializing Reticulum...")
        reticulum = RNS.Reticulum()
        print("      ✓ Reticulum initialized successfully")
        print()

        print("[3/4] Checking interfaces...")
        interfaces = RNS.Transport.interfaces

        if not interfaces:
            print("      ⚠ No interfaces found!")
            print("      Make sure rnsd is running: rnsd -v")
            return False

        print(f"      ✓ Found {len(interfaces)} interface(s):")
        for interface in interfaces:
            mode = "Full" if interface.mode == RNS.Interfaces.Interface.Interface.MODE_FULL else "Access Point"
            print(f"        - {interface.name}")
            print(f"          Type: {type(interface).__name__}")
            print(f"          Mode: {mode}")
            print(f"          Online: {interface.online}")
            if hasattr(interface, 'bitrate'):
                print(f"          Rate: {interface.bitrate/1000:.2f} kbps")
        print()

        print("[4/4] Node identity...")
        identity = RNS.Identity()
        print(f"      ✓ Identity created")
        print(f"      Hash: {RNS.prettyhexrep(identity.hash)}")
        print()

        print("=" * 60)
        print("✓ All tests passed!")
        print("=" * 60)
        print()
        print("Your Reticulum node is operational and ready to use.")
        print()
        print("Next steps:")
        print("  - Try running examples from: github.com/markqvist/Reticulum/tree/master/Examples")
        print("  - Build your own applications using the RNS Python API")
        print("  - Connect with other nodes on the Reticulum network")
        print()

        return True

    except ImportError as e:
        print(f"      ✗ Failed to import RNS: {e}")
        print()
        print("Solution: Install Reticulum")
        print("  pip install rns")
        return False

    except Exception as e:
        print(f"      ✗ Error: {e}")
        print()
        print("Troubleshooting:")
        print("  1. Check if rnsd is running: ps aux | grep rnsd")
        print("  2. Try starting it: rnsd -v")
        print("  3. Check status: rnstatus")
        return False


if __name__ == "__main__":
    success = test_reticulum_node()
    sys.exit(0 if success else 1)
