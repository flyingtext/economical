# 📑 Economical 권한 매트릭스

Economical 플랫폼의 전체 사이트맵에 대해 **화면 × 데이터 요소 × CRUD × Role** 매핑을 정리한 문서입니다.  
Role 계층: **Owner > Admin > Contributor > Viewer > Guest**

---

## Role 정의

- **Owner**: 모든 권한 보유, 팀/리소스 최종 책임자
- **Admin**: Owner 제외 전 권한, 팀 관리 및 리소스 제어 가능
- **Contributor**: Create/Update/Execute 가능, Delete 제한
- **Viewer**: Read 전용, 일부 Export 가능
- **Guest**: 퍼블릭 리소스만 Read

---

## 권한 매트릭스

| 카테고리 | 화면 | 주요 데이터 요소 | CRUD | Owner | Admin | Contributor | Viewer | Guest |
|----------|------|-----------------|------|-------|-------|-------------|--------|-------|
| 계정 | 내 계정 설정 | email, password, locale, backup link | U | ✅ | – | – | – | – |
| 계정 | 로그인/회원가입 | email, password | C/R | ✅ | – | – | – | – |
| 팀 | 팀원 관리 | team_members(role, last_activity) | C/R/U/D | ✅ | ✅ | – | R | – |
| 팀 | 크레딧 관리 | balance, usage_log | R/U | ✅ | ✅ | – | R | – |
| 팀 | 팀 설정 | name, description | U | ✅ | ✅ | – | – | – |
| 모델 | 모델 리스트 | name, owner, status, created_at | C/R | ✅ | ✅ | ✅ | R | Public only |
| 모델 | 모델 상세 | desc, version, owner | U/D | ✅ | ✅ | U | R | – |
| 모델 | 모델 실행 결과 | params, result, status | C/R/D | ✅ | ✅ | C/R | R | – |
| 모델 | 모델 쇼케이스 | title, viz, rating | C/R/U/D | ✅ | ✅ | C/U | R | R |
| 모델 | 모델 파이프라인 | graph_nodes, connections | C/R/U/D | ✅ | ✅ | C/U | R | – |
| 모델 | 시나리오 러너 | scenario_inputs, comparison_viz | C/R | ✅ | ✅ | C/R | R | – |
| 데이터 | 데이터셋 리스트 | name, schema, status | C/R | ✅ | ✅ | C/R | R | Public only |
| 데이터 | 데이터셋 상세 | description, schema, row_count | U/D | ✅ | ✅ | U | R | – |
| 데이터 | 데이터 프리뷰 | sample rows, columns | R | ✅ | ✅ | C | R | – |
| 데이터 | 데이터 평가 | score, comment | C/R/U/D(본인) | ✅ | ✅ | C/U | R | R |
| 데이터 | 데이터 업로드 | file, metadata, scope | C | ✅ | ✅ | C | – | – |
| 데이터 | 데이터 요청 | request_form, status | C/R/U | ✅ | ✅ | C | R | – |
| 대시보드 | 개인 대시보드 | widget configs | C/R/U/D | ✅ | – | C/U | R | – |
| 대시보드 | 팀 대시보드 | team widgets | C/R/U/D | ✅ | ✅ | C/U | R | – |
| 대시보드 | 공유된 대시보드 | public dashboards | R | ✅ | ✅ | ✅ | R | R |
| 커뮤니티 | 피드백(좋아요/댓글) | like, comment | C/R/U/D(본인) | ✅ | ✅ | C/U | R | R |
| 커뮤니티 | 알림센터 | notifications | R | ✅ | ✅ | C | R | – |
| 커뮤니티 | 구독 랭킹 | rank_list | R | ✅ | ✅ | ✅ | R | R |
| GIS | 맵 뷰 | geojson layers, metrics | R | ✅ | ✅ | C | R | – |
| GIS | 로케일 기반 시각화 | region_locale, viz | R | ✅ | ✅ | C | R | – |
| GIS | 실시간 예측 뷰 | prediction_stream | R | ✅ | ✅ | C | R | – |
| API | 모델 API | endpoint, token | C/R/D | ✅ | ✅ | – | – | – |
| API | 데이터 API | endpoint, token | C/R/D | ✅ | ✅ | – | – | – |
| API | API 키 관리 | key_id, scope | C/R/U/D | ✅ | ✅ | – | – | – |
| Admin | 사용자 관리 | users.* | C/R/U/D | – | ✅ | – | – | – |
| Admin | 모델 관리 | models.* | C/R/U/D | – | ✅ | – | – | – |
| Admin | 데이터 관리 | datasets.* | C/R/U/D | – | ✅ | – | – | – |
| Admin | 커뮤니티 관리 | comments, likes | C/R/U/D | – | ✅ | – | – | – |
| Admin | 로그/DB 현황 | audit_logs.* | R | – | ✅ | – | – | – |
| Admin | 시스템 설정 | configs | U | – | ✅ | – | – | – |
| Admin | 시스템 통계 | usage_stats | R | – | ✅ | – | – | – |
| Admin | 자동 크레딧 관리 | rules, balances | U | – | ✅ | – | – | – |

---

✅ = 허용, – = 불가, R/U/C/D = 해당 CRUD 권한
