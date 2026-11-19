# 旧版からの更新

## v0.5.1 / v0.5.2からの更新

「想定外のダウンロードURLです」は旧版が改名前のリポジトリURLを検証するため発生します。v0.5.3以降で修正済みですが、旧版からは初回だけ[ReleaseのQPKG](https://github.com/souten-yd/PatentBuddy/releases/latest)をQNAP App Centerの手動インストールで上書き更新してください。既存アプリをアンインストールしないでください。内部ID `QnapLibrary` と既存の `QnapLibrary-data` は維持します。QTS実機の更新完了は別途確認が必要です。

v0.5.2の実コードと公式v0.5.4 Releaseで同じ例外を再現しています。更新後は管理画面のversionと既存資料・ログインを確認してください。自動更新のv0.5.3→v0.5.4はLinuxパッケージで検証済みです。QNAPでの手動更新成功とは区別しています。

## ResearchDataHub独立リポジトリへの更新（2026-11-19）

- サーバー/QPKGの配布先: https://github.com/souten-yd/ResearchDataHub/releases/latest
- 旧v0.5.12以下はPatentBuddyリリースしか確認しません。旧Repoで配布予定のv0.5.13更新ブリッジで新Repoへ切替えるか、新Repoのv0.5.14 QPKGをQTS App Centerでアンインストールせず上書きしてください。ブリッジ公開までは自動移行できません。
- QPKG ID QnapLibrary、データフォルダ QnapLibrary-data、ポート17871、設定/パスキーRP IDは維持します。更新前は整合したSQLiteバックアップとsettings/secretsを保全し、health/ログイン/件数/検索を検証してください。
- Linuxでは既存サービスと新入口の両方を維持します。PCとNASで同一SQLiteを同時書込みしないでください。
