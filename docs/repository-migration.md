# ResearchDataHubリポジトリ移管・QNAP/Linux互換契約（2026-11-19）

## 正本と移管状況
- サーバー/QNAP QPKG/Linux tar.gzの正本: https://github.com/souten-yd/ResearchDataHub
- PatentBuddy ControlDeck特許アドオンの正本: https://github.com/souten-yd/PatentBuddy
- REST/MCP、収集、規格/特許/論文の保存、検索、認証、バックアップはResearchDataHub側が所有。未公開発明の外部LLM送信は禁止。
- 初期移管は動作互換のため旧qnaplibrary実装と特許/アドオンモジュールをまとめて複製。完全な特許コード分離と旧Repoの重複削除は未完。新Repoのaddon.jsonやアドオンコードは移行期の互換用で、PatentBuddy機能追加の正本にしない。

## QNAPおよびLinuxの非破壊互換
- QPKG ID QnapLibrary、永続フォルダ QnapLibrary-data、内部import qnaplibrary、ポート17871、Cookie/CSRF、パスキーRP ID、既存DB schema/設定/秘密情報/REST APIを変更しない。
- Linuxの ./rdh.sh doctor|serve|test および python3 -m researchdatahub と既存ランチャーの双方を維持。QPKGには同一サーバーとresearchdatahub入口を同梱。
- 既存のQPKGをアンインストールせず上書きする。NASとPC間で動作中のSQLite/WALを共有・二重書込みしない。データ移行は整合バックアップ、SHA/quick_check、認証・件数照合後に単一writerへ切替える。
- アップデータは新Repoの厳格なSHA-256・Release URL検証を維持。無条件のfallback/redirectを増やさない。

## 旧版から新Repoへの更新
- v0.5.12以前のアプリはPatentBuddy Releasesを検索するため新Repoのv0.5.14を自動検出できない。
- 旧Repoのv0.5.13を更新ブリッジとして新Repoに更新先を切替える予定。旧RepoでReleaseが実際に公開されるまでは自動移行未完成。
- 代替は新Repoのv0.5.14 QPKGの手動上書き。Linuxは旧版バックアップ・SHA検証・再起動/ロールバックで移行。
- PatentBuddy側のQPKGリリース停止とアドオン単独化は、更新ブリッジの公開/検証後の別PRで実施し、既存ユーザーの更新経路を断たない。

## 必須の検証
- bash scripts/verify.sh、bash scripts/build-linux.sh dist、bash scripts/build-qpkg.sh dist、scripts/inspect-qpkg.py を全件実施。
- Linuxで旧/新両入口のhealth、ログイン、パスキー、MCP、文献保存・検索・バックアップと再起動継続を確認。
- QNAPでは自動起動/停止、アンインストールなし上書き、データ/パスキー保全、I/O/実機レグレッションを確認。Linux上のQPKG展開テストだけをQTS実機試験としない。
- backend authoritative、現行default UI維持、権限/CSRF/privacy gateを緩めず、Vue default化・任意コマンド実行・起動時npm buildは追加しない。
