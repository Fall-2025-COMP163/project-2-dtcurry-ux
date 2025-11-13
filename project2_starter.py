import pytest
"""
COMP 163 - Project 2: Character Abilities Showcase
Name: [Curry, Curry]
Date: [11/13/2025]

AI Usage: [Document any AI assistance used]
Example: AI helped with inheritance structure and method overriding concepts
"""

# ============================================================================
# PROVIDED BATTLE SYSTEM (DO NOT MODIFY)
# ============================================================================

class SimpleBattle:
    """
    Simple battle system provided for you to test your characters.
    DO NOT MODIFY THIS CLASS - just use it to test your character implementations.
    """
    
    def __init__(self, character1, character2):
        self.char1 = character1
        self.char2 = character2
    
    def fight(self):
        """Simulates a simple battle between two characters"""
        print(f"\n=== BATTLE: {self.char1.name} vs {self.char2.name} ===")
        
        # Show starting stats
        print("\nStarting Stats:")
        self.char1.display_stats()
        self.char2.display_stats()
        
        print(f"\n--- Round 1 ---")
        print(f"{self.char1.name} attacks:")
        self.char1.attack(self.char2)
        
        if self.char2.health > 0:
            print(f"\n{self.char2.name} attacks:")
            self.char2.attack(self.char1)
        
        print(f"\n--- Battle Results ---")
        self.char1.display_stats()
        self.char2.display_stats()
        
        if self.char1.health > self.char2.health:
            print(f" {self.char1.name} wins!")
        elif self.char2.health > self.char1.health:
            print(f" {self.char2.name} wins!")
        else:
            print(" It's a tie!")

# ============================================================================
# YOUR CLASSES TO IMPLEMENT (6 CLASSES TOTAL)
# ============================================================================

import random

class Character:
    """
    Base class for all characters.
    This is the top of our inheritance hierarchy.
    """
    
    def __init__(self, name, health, strength, magic):
        """Initialize basic character attributes"""
        self.name = name
        self.health = health
        self.strength = strength
        self.magic = magic
        
    def attack(self, target):
        """
        Basic attack method that all characters can use.
        Damage = strength
        """
        damage = self.strength
        print(f"{self.name} attacks {target.name} for {damage} damage!")
        target.take_damage(damage)
        
    def take_damage(self, damage):
        """Reduce health but never below 0"""
        self.health = max(0, self.health - damage)
        print(f"{self.name} now has {self.health} HP.")
        
    def display_stats(self):
        """Show basic stats"""
        print(f"=== {self.name} ===")
        print(f"Health: {self.health}")
        print(f"Strength: {self.strength}")
        print(f"Magic: {self.magic}")


class Player(Character):
    """Base class for player characters"""
    
    def __init__(self, name, character_class, health, strength, magic):
        super().__init__(name, health, strength, magic)
        self.character_class = character_class
        self.level = 1
        self.experience = 0
        
    def display_stats(self):
        super().display_stats()
        print(f"Class: {self.character_class}")
        print(f"Level: {self.level}")
        print(f"Experience: {self.experience}")


class Warrior(Player):
    """Warrior class"""
    
    def __init__(self, name):
        super().__init__(name, "Warrior", 120, 15, 5)
        
    def attack(self, target):
        damage = self.strength + 5
        print(f"{self.name} swings a mighty sword for {damage} damage!")
        target.take_damage(damage)
        
    def power_strike(self, target):
        damage = self.strength * 2
        print(f"{self.name} uses Power Strike on {target.name} for {damage} damage!")
        target.take_damage(damage)


class Mage(Player):
    """Mage class"""
    
    def __init__(self, name):
        super().__init__(name, "Mage", 80, 8, 20)
        
    def attack(self, target):
        damage = self.magic
        print(f"{self.name} casts a magic bolt for {damage} damage!")
        target.take_damage(damage)
        
    def fireball(self, target):
        damage = self.magic * 2
        print(f"{self.name} hurls a Fireball at {target.name} for {damage} damage!")
        target.take_damage(damage)


class Rogue(Player):
    """Rogue class"""
    
    def __init__(self, name):
        super().__init__(name, "Rogue", 90, 12, 10)
        
    def attack(self, target):
        damage = self.strength
        # 30% chance for critical hit
        if random.randint(1, 10) <= 3:
            damage *= 2
            print(f"Critical hit! {self.name} deals {damage} damage!")
        else:
            print(f"{self.name} strikes for {damage} damage!")
        target.take_damage(damage)
        
    def sneak_attack(self, target):
        damage = self.strength * 2
        print(f"{self.name} performs Sneak Attack for {damage} damage!")
        target.take_damage(damage)


class Weapon:
    """Weapon class for composition"""
    
    def __init__(self, name, damage_bonus):
        self.name = name
        self.damage_bonus = damage_bonus
        
    def display_info(self):
        print(f"Weapon: {self.name} | Damage Bonus: {self.damage_bonus}")


# ============================================================================
# MAIN PROGRAM FOR TESTING (YOU CAN MODIFY THIS FOR TESTING)
# ============================================================================

if __name__ == "__main__":
    print("=== CHARACTER ABILITIES SHOWCASE ===")
    print("Testing inheritance, polymorphism, and method overriding")
    print("=" * 50)
    
    # Create one of each character type
    warrior = Warrior("Sir Galahad")
    mage = Mage("Merlin")
    rogue = Rogue("Robin Hood")
    
    # Display their stats
    print("\n Character Stats:")
    warrior.display_stats()
    print("-" * 30)
    mage.display_stats()
    print("-" * 30)
    rogue.display_stats()
    
    # Test polymorphism - same method call, different behavior
    print("\n Testing Polymorphism (same attack method, different behavior):")
    dummy_target = Character("Target Dummy", 100, 0, 0)
    
    for character in [warrior, mage, rogue]:
        print(f"\n{character.name} attacks the dummy:")
        character.attack(dummy_target)
        dummy_target.health = 100  # Reset dummy health
    
    # Test special abilities
    print("\n Testing Special Abilities:")
    target1 = Character("Enemy1", 50, 0, 0)
    target2 = Character("Enemy2", 50, 0, 0)
    target3 = Character("Enemy3", 50, 0, 0)
    
    warrior.power_strike(target1)
    mage.fireball(target2)
    rogue.sneak_attack(target3)
    
    # Test composition with weapons
    print("\n Testing Weapon Composition:")
    sword = Weapon("Iron Sword", 10)
    staff = Weapon("Magic Staff", 15)
    dagger = Weapon("Steel Dagger", 8)
    
    sword.display_info()
    staff.display_info()
    dagger.display_info()
    
    # Test the battle system
    print("\n Testing Battle System:")
    battle = SimpleBattle(warrior, mage)
    battle.fight()
    
    print("\n Testing complete!")   
