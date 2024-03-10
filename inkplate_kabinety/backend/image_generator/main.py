import yaml
import csv
import downloader
import card_generator


def main():
    """Main function to run the image generator."""
    # Read config file
    with open("config.yaml", "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    # Read teachers data
    with open(f"../{config['data_file']}", "r", encoding="utf-8") as file:
        teachers = list(
            csv.DictReader(
                file, delimiter=";", fieldnames=["name", "subjects", "image_url"]
            )
        )
        # ignore header
        teachers = teachers[1:]

    # Download images
    # for teacher in teachers:
    #     downloader.download_teacher_image(teacher)

    # Create cards
    teachers = teachers[:3]
    names = [teacher["name"] for teacher in teachers]
    subjects = [teacher["subjects"] for teacher in teachers]

    card_generator.create_card(names, subjects, config["template_file"], "card")


if __name__ == "__main__":
    main()
