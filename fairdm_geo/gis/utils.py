# import requests
from django.core.management import call_command
from django.db.utils import DEFAULT_DB_ALIAS


def get_compression_formats():
    return ["bz2", "gz", "lzma", "xz"]


def splitext(text):
    file_parts = text.split(".")

    if len(file_parts) == 2:
        fname = ".".join(file_parts[:-1])

        return fname, file_parts[-1].lower(), None

    elif len(file_parts) == 3:
        fname = ".".join(file_parts[:-2])
        file_format = file_parts[-2].lower()
        compression_format = file_parts[-1].lower()
        return fname, file_format, compression_format


def save_uploaded_file_on_disk(uploaded_file, destination_path):
    with open(destination_path, "wb") as fp:
        for chunk in uploaded_file.chunks():
            fp.write(chunk)


def load_fixtures(fixtures):
    call_command(
        "loaddata",
        fixtures,
        **{
            "ignore": True,
            "database": DEFAULT_DB_ALIAS,
            "verbosity": 1,
        },
    )


# def load_online_fixtures(url):
#     r = requests.get(url, timeout=5)
#     if r.status_code == 200:
#         fname = os.path.basename(url)

#         _, ftype, comptype = splitext(fname)

#         fd, destination_path = tempfile.mkstemp(fname)

#         upload = SimpleUploadedFile(destination_path, r.content)

#         save_uploaded_file_on_disk(upload, destination_path)

#         load_fixtures(destination_path)

#         os.close(fd)
#         os.unlink(destination_path)
#     else:
#         raise ValidationErr("The online file could not be found.")
