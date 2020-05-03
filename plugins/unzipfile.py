# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# # (c) Shrimadhav U K

# # the logging things
# import logging
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# logger = logging.getLogger(__name__)

# import os
# import shutil
# import subprocess
# import time
# from helper_funcs.display_progress import humanbytes, progress_for_pyrogram
# # the secret configuration specific things
# if bool(os.environ.get("WEBHOOK", False)):
#     from sample_config import Config
# else:
#     from sample_config import Config

# # the Strings used for this "thing"
# from translation import Translation

# import pyrogram
# logging.getLogger("pyrogram").setLevel(logging.WARNING)

# from helper_funcs.chat_base import TRChatBase
# from helper_funcs.display_progress import progress_for_pyrogram, humanbytes


# @pyrogram.Client.on_message(pyrogram.Filters.command(["zipcikar"]))
# async def unzip(bot, update):
#     if update.from_user.id not in Config.AUTH_USERS:
#         await bot.delete_messages(
#             chat_id=update.chat.id,
#             message_ids=update.message_id,
#             revoke=True
#         )
#         return
#     TRChatBase(update.from_user.id, update.text, "unzip")
#     saved_file_path = Config.DOWNLOAD_LOCATION + \
#         "/" + str(update.from_user.id) + ".unzip.zip"
#     if os.path.exists(saved_file_path):
#         os.remove(saved_file_path)
#     reply_message = update.reply_to_message
#     if ((reply_message is not None) and
#         (reply_message.document is not None) and
#         (reply_message.document.file_name.endswith(Translation.UNZIP_SUPPORTED_EXTENSIONS))):
#         a = await bot.send_message(
#             chat_id=update.chat.id,
#             text=Translation.DOWNLOAD_START,
#             reply_to_message_id=update.message_id
#         )
#         c_time = time.time()
#         try:
#             await bot.download_media(
#                 message=reply_message,
#                 file_name=saved_file_path,
#                 progress=progress_for_pyrogram,
#                 progress_args=(
#                     Translation.DOWNLOAD_START,
#                     a,
#                     c_time
#                 )
#             )
#         except (ValueError) as e:
#             await bot.edit_message_text(
#                 chat_id=update.chat.id,
#                 text=str(e),
#                 message_id=a.message_id
#             )
#         else:
#             await bot.edit_message_text(
#                 chat_id=update.chat.id,
#                 text=Translation.SAVED_RECVD_DOC_FILE,
#                 message_id=a.message_id
#             )
#             extract_dir_path = Config.DOWNLOAD_LOCATION + \
#                 "/" + str(update.from_user.id) + "zipped" + "/"
#             if not os.path.isdir(extract_dir_path):
#                 os.makedirs(extract_dir_path)
#             await bot.edit_message_text(
#                 chat_id=update.chat.id,
#                 text=Translation.EXTRACT_ZIP_INTRO_THREE,
#                 message_id=a.message_id
#             )
#             try:
#                 command_to_exec = [
#                     "unzip",
#                     "-o",
#                     saved_file_path,
#                     # extract_dir_path,
#                     "-d",
#                     extract_dir_path
#                 ]
#             filename = sorted(get_lst_of_files(extract_dir_path, []))
#                 # https://stackoverflow.com/a/39629367/4723940
#             await event.edit("Unzipping now")
#                 # r=root, d=directories, f = files
#             for single_file in filename:
#                 if os.path.exists(single_file):
#                 # https://stackoverflow.com/a/678242/4723940
#                     caption_rts = os.path.basename(single_file)
#                     force_document = False
#                     supports_streaming = True
#                     document_attributes = []
#                     if single_file.endswith((".mp4", ".mp3", ".flac", ".webm")):
#                         metadata = extractMetadata(createParser(single_file))
#                         duration = 0
#                         width = 0
#                         height = 0
#                         if metadata.has("duration"):
#                             duration = metadata.get('duration').seconds
#                         if os.path.exists(thumb_image_path):
#                             metadata = extractMetadata(createParser(thumb_image_path))
#                             if metadata.has("width"):
#                                 width = metadata.get("width")
#                             if metadata.has("height"):
#                                 height = metadata.get("height")
#                         document_attributes = [
#                             DocumentAttributeVideo(
#                                 duration=duration,
#                                 w=width,
#                                 h=height,
#                                 round_message=False,
#                                 supports_streaming=True
#                             )
#                         ]
#                     try:
#                         await bot.send_file(
#                             update.chat_id,
#                             single_file,
#                             caption=f"UnZipped `{caption_rts}`",
#                             force_document=force_document,
#                             supports_streaming=supports_streaming,
#                             allow_cache=False,
#                             reply_to=update.message.id,
#                             attributes=document_attributes,
#                                 # progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
#                                 #     progress(d, t, event, c_time, "trying to upload")
#                                 # )
#                         )
#                     except Exception as e:
#                         await bot.send_message(
#                             update.chat_id,
#                             "{} caused `{}`".format(caption_rts, str(e)),
#                             reply_to=update.message.id
#                         )
#                             # some media were having some issues
#                         continue
#                     os.remove(single_file)
#             os.remove(downloaded_file_name)



# def get_lst_of_files(input_directory, output_lst):
#     filesinfolder = os.listdir(input_directory)
#     for file_name in filesinfolder:
#         current_file_name = os.path.join(input_directory, file_name)
#         if os.path.isdir(current_file_name):
#             return get_lst_of_files(current_file_name, output_lst)
#         output_lst.append(current_file_name)
#     return output_lst
