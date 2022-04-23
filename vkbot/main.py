import vk_api


def main():

    login, password = 'python@vk.com', 'mypassword'
    vk_session = vk_api.VkApi(login, password)

    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    upload = vk_api.VkUpload(vk_session)

    photo = upload.photo(  # Подставьте свои данные
        'ars.png',
        album_id=200851098,
        group_id=74030368
    )

    vk_photo_url = 'https://vk.com/photo{}_{}'.format(
        photo[0]['owner_id'], photo[0]['id']
    )

    print(photo, '\nLink: ', vk_photo_url)


if __name__ == '__main__':
    main()