import yaml
import downloader
import csv


def main():
    """Main function to run the image generator."""
    # Read teachers data
    with open("../teachers.csv", "r", encoding="utf-8") as file:
        teachers = list(
            csv.DictReader(
                file, delimiter=";", fieldnames=["name", "subjects", "image_url"]
            )
        )

    # Download images
    # for teacher in teachers:
    #     downloader.download_teacher_image(teacher)


if __name__ == "__main__":
    main()
