import sys
import os
import shutil

TARGET_BUILD_DIRECTORY_NAME = "build"
TARGET_STATIC_DIRECTORY_NAME = "static"
TARGET_CSS_DIRECTORY_NAME = "css"
TARGET_JS_DIRECTORY_NAME = "js"
TARGET_IMAGE_DIRECTORY_NAME = "img"

SOURCE_BUILD_DIRECTORY_NAME = "build"
SOURCE_STATIC_DIRECTORY_NAME = "static"
SOURCE_CSS_DIRECTORY_NAME = "css"
SOURCE_JS_DIRECTORY_NAME = "js"
SOURCE_IMAGE_DIRECTORY_NAME = "img"


def create_build_directory(directory):
    build_dir = os.path.join(directory, TARGET_BUILD_DIRECTORY_NAME)
    try:
        os.mkdir(build_dir)
    except OSError:
        print("Build failed: Couldn't create build directory")
        exit(1)

    return build_dir


def create_static_directory(directory):
    static_dir = os.path.join(directory, TARGET_STATIC_DIRECTORY_NAME)
    try:
        os.mkdir(static_dir)
    except OSError:
        print("Build failed: Couldn't create static directory")
        exit(1)

    return static_dir


def create_css_directory(directory):
    css_dir = os.path.join(directory, TARGET_CSS_DIRECTORY_NAME)
    try:
        os.mkdir(css_dir)
    except OSError:
        print("Build failed: Couldn't create css directory")
        exit(1)

    return css_dir


def create_js_directory(directory):
    js_dir = os.path.join(directory, TARGET_JS_DIRECTORY_NAME)
    try:
        os.mkdir(js_dir)
    except OSError:
        print("Build failed: Couldn't create js directory")
        exit(1)

    return js_dir


def create_image_directory(directory):
    image_dir = os.path.join(directory, TARGET_IMAGE_DIRECTORY_NAME)
    try:
        os.mkdir(image_dir)
    except OSError:
        print("Build failed: Couldn't create image directory")
        exit(1)

    return image_dir


def create_structure_directories():
    cur_dir = os.getcwd()
    build_dir = create_build_directory(cur_dir)
    static_dir = create_static_directory(build_dir)
    css_dir = create_css_directory(static_dir)
    js_dir = create_js_directory(static_dir)


def remove_build_directory_if_exists():
    cur_dir = os.getcwd()
    target_build_directory = os.path.join(cur_dir, TARGET_BUILD_DIRECTORY_NAME)
    if os.path.exists(target_build_directory):
        shutil.rmtree(target_build_directory)


def copy_to_build(source_path):
    copy_static_files(source_path)
    source_build_path = os.path.join(source_path, SOURCE_BUILD_DIRECTORY_NAME)
    copy_html_files(source_build_path)
    copy_ico_files(source_build_path)
    copy_png_files(source_build_path)
    # copy_js_files(source_build_path)
    # copy_json_files(source_build_path)
    # TODO to handle service-worker.js file


def copy_ico_files(source_path):

    cur_dir = os.getcwd()
    target_build_path = os.path.join(cur_dir, TARGET_BUILD_DIRECTORY_NAME)

    for file in os.listdir(source_path):
        file_abs_path = os.path.join(source_path, file)
        file_abs_path_destination = os.path.join(target_build_path, file)
        if file_abs_path.endswith(".ico"):
            shutil.copyfile(file_abs_path, file_abs_path_destination)


def copy_png_files(source_path):

    cur_dir = os.getcwd()
    target_build_path = os.path.join(cur_dir, TARGET_BUILD_DIRECTORY_NAME)

    for file in os.listdir(source_path):
        file_abs_path = os.path.join(source_path, file)
        file_abs_path_destination = os.path.join(target_build_path, file)
        if file_abs_path.endswith(".png"):
            shutil.copyfile(file_abs_path, file_abs_path_destination)


def copy_json_files(source_path):

    cur_dir = os.getcwd()
    target_build_path = os.path.join(cur_dir, TARGET_BUILD_DIRECTORY_NAME)

    for file in os.listdir(source_path):
        file_abs_path = os.path.join(source_path, file)
        file_abs_path_destination = os.path.join(target_build_path, file)
        if file_abs_path.endswith(".json"):
            shutil.copyfile(file_abs_path, file_abs_path_destination)


def copy_html_files(source_path):

    cur_dir = os.getcwd()
    target_build_path = os.path.join(cur_dir, TARGET_BUILD_DIRECTORY_NAME)

    for file in os.listdir(source_path):
        file_abs_path = os.path.join(source_path, file)
        file_abs_path_destination = os.path.join(target_build_path, file)
        if file_abs_path.endswith(".html"):
            shutil.copyfile(file_abs_path, file_abs_path_destination)


def copy_js_files(source_path):

    cur_dir = os.getcwd()
    target_build_path = os.path.join(cur_dir, TARGET_BUILD_DIRECTORY_NAME)

    for file in os.listdir(source_path):
        file_abs_path = os.path.join(source_path, file)
        file_abs_path_destination = os.path.join(target_build_path, file)
        if file_abs_path.endswith(".js"):
            shutil.copyfile(file_abs_path, file_abs_path_destination)


def copy_static_files(source_path):

    source_build_path = os.path.join(source_path, SOURCE_BUILD_DIRECTORY_NAME)
    source_static_path = os.path.join(source_build_path, SOURCE_STATIC_DIRECTORY_NAME)
    source_css_path = os.path.join(source_static_path, SOURCE_CSS_DIRECTORY_NAME)
    source_js_path = os.path.join(source_static_path, SOURCE_JS_DIRECTORY_NAME)

    cur_dir = os.getcwd()
    target_build_path = os.path.join(cur_dir, TARGET_BUILD_DIRECTORY_NAME)
    target_static_path = os.path.join(target_build_path, TARGET_STATIC_DIRECTORY_NAME)
    target_css_path = os.path.join(target_static_path, TARGET_CSS_DIRECTORY_NAME)
    target_js_path = os.path.join(target_static_path, TARGET_JS_DIRECTORY_NAME)

    copy_all_files_from_directory(source_css_path, target_css_path)
    copy_all_files_from_directory(source_js_path, target_js_path)


def copy_all_files_from_directory(source, destination):

    for file in os.listdir(source):
        file_abs_path = os.path.join(source, file)
        file_abs_path_destination = os.path.join(destination, file)
        shutil.copyfile(file_abs_path, file_abs_path_destination)


def main():

    remove_build_directory_if_exists()
    create_structure_directories()
    n_args = len(sys.argv)
    for i in range(1, n_args):
        copy_to_build(os.path.abspath(sys.argv[i]))


if __name__ == '__main__':
    main()
