#!/usr/bin/env python3
"""
Hello World Skill - Example V2 Skill Implementation
Demonstrates goal-driven design with testable features
"""

import argparse
from datetime import datetime


def get_time_greeting():
    """Determine greeting based on current time of day"""
    hour = datetime.now().hour
    
    if 5 <= hour < 12:
        return "Good morning"
    elif 12 <= hour < 18:
        return "Good afternoon"
    elif 18 <= hour < 21:
        return "Good evening"
    else:
        return "Good night"


def generate_greeting(name, use_time=False, custom_message=None):
    """
    Generate a personalized greeting
    
    Args:
        name: Name to greet
        use_time: Whether to include time-based prefix
        custom_message: Custom message to use instead of default
    
    Returns:
        Formatted greeting string
    """
    if not name or not name.strip():
        raise ValueError("Name cannot be empty")
    
    # Capitalize name
    name = name.strip().title()
    
    # Determine greeting prefix
    if custom_message:
        prefix = custom_message.strip()
    elif use_time:
        prefix = get_time_greeting()
    else:
        prefix = "Hello"
    
    return f"{prefix}, {name}!"


def main():
    parser = argparse.ArgumentParser(
        description="Generate personalized greetings"
    )
    parser.add_argument(
        "name",
        help="Name to greet"
    )
    parser.add_argument(
        "--time",
        action="store_true",
        help="Include time-based greeting"
    )
    parser.add_argument(
        "--message",
        help="Custom greeting message"
    )
    
    args = parser.parse_args()
    
    try:
        greeting = generate_greeting(
            args.name,
            use_time=args.time,
            custom_message=args.message
        )
        print(greeting)
    except ValueError as e:
        print(f"Error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
