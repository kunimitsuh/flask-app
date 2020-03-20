
## GCRにpush

Googleの[公式ドキュメント](https://cloud.google.com/container-registry/docs/pushing-and-pulling?authuser=1)に記載がある
>gcloud を認証ヘルパーとして使用するように Docker を構成しているか、Docker で別の認証方法を使用していること。gcloud を認証ヘルパーとして使用するには、次のコマンドを実行します。

```sh
> gcloud auth configure-docker
```

hostname削除はこちらの[issue](https://github.com/GoogleCloudPlatform/docker-credential-gcr/issues/11#issuecomment-384709217)からたどる


```sh
# tag付け
> docker tag [SOURCE_IMAGE] [HOSTNAME]/[PROJECT-ID]/[IMAGE]

# gcrにpush
> docker push [HOSTNAME]/[PROJECT-ID]/[IMAGE]

# 確認
> gcloud container images list-tags [HOSTNAME]/[PROJECT-ID]/[IMAGE]
```

GCPコンソールのContainer Registryで確認


## Cloud SQLの設定 [mysql doc](https://cloud.google.com/sql/docs/mysql/create-manage-users?hl=ja)[postgres doc](https://cloud.google.com/sql/docs/postgres/create-manage-users?hl=ja)
default user(postgres)のパスワード設定
```console
gcloud sql users set-password postgres \
  --instance=[INSTANCE_NAME] --prompt-for-password
```
新規ユーザー作成
```console
gcloud sql users create [USER_NAME] \
  --instance=[INSTANCE_NAME] --password=[PASSWORD]
```
ユーザーパスワード変更
```console
gcloud sql users set-password [USER_NAME] \
  --instance=[INSTANCE_NAME] --prompt-for-password
```
