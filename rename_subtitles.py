import os
import argparse
import re


def get_episode_number(file, regex_file):
    result = None
    regex = re.compile(regex_file)
    matches = regex.findall(file)
    if len(matches):
        result = tuple([x.lstrip('0') for x in matches[0]])
    return result


def get_files(directory, ext, regex_file):
    result = {}

    for file in os.listdir(directory):
        _, file_ext = os.path.splitext(file)
        if ext == file_ext.replace('.', ''):
            full_path = os.path.join(directory, file)
            episode_number = get_episode_number(file, regex_file)

            if episode_number is None:
                print("Failed to compute the episode number for %s" % full_path)
                continue

            result[episode_number] = full_path

    return result


def main():
    p = argparse.ArgumentParser()
    p.add_argument('-d', '--directory', required=True)
    p.add_argument('-s', '--subtitle-ext', required=True)
    p.add_argument('-e', '--episode-ext', required=True)
    p.add_argument('--regex-episode', required=True)
    p.add_argument('--regex-subtitle', required=True)

    args = p.parse_args()
    episodes = get_files(
        args.directory, args.episode_ext, args.regex_episode)
    subtitles = get_files(
        args.directory, args.subtitle_ext, args.regex_subtitle)

    for item in episodes:
        episode_name = episodes[item]
        episode_name_without_ext, _ = os.path.splitext(episode_name)
        new_subtitle_name = episode_name_without_ext + "." + args.subtitle_ext

        if item in subtitles:
            os.rename(subtitles[item], new_subtitle_name)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
