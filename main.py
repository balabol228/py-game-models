import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    def main():
        import json

        with open("players.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        for player in data:
            race_data = player["race"]

            race, created = Race.objects.get_or_create(
                name=race_data["name"],
                defaults={
                    "description": race_data.get("description", "")
                }
            )

            guild_data = player["guild"]

            guild, created = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={
                    "description": guild_data.get("description", "")
                }
            )

            Player.objects.create(
                nickname=player["nickname"],
                email=player["email"],
                bio=player["bio"],
                race=race,
                guild=guild
            )

            for skill_data in player["skills"]:
                skill, created = Skill.objects.get_or_create(
                    name=skill_data["name"],
                    defaults={
                        "bonus": skill_data.get("bonus", ""),
                        "race": race
                    }
                )
    pass


if __name__ == "__main__":
    main()
