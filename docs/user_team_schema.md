# 📑 User & Team Database Schema

Economical 플랫폼의 **사용자(User) 및 팀(Team)** 관리에 필요한 DB 테이블 설계입니다.  
RBAC(Role-Based Access Control), 크레딧 시스템, API 발급, 백업 관리까지 포함합니다.

---

## 1. USERS

| 컬럼명         | 타입        | 제약조건            | 설명 |
|----------------|------------|---------------------|------|
| id             | BIGSERIAL  | PK                  | 사용자 고유 ID |
| email          | VARCHAR    | UNIQUE, NOT NULL    | 로그인 이메일 |
| password_hash  | VARCHAR    | NOT NULL            | 해시된 비밀번호 |
| name           | VARCHAR    |                     | 사용자 이름 |
| locale         | VARCHAR    | DEFAULT 'en'        | 언어/지역 설정 |
| currency_pref  | VARCHAR    | DEFAULT 'USD'       | 기본 화폐 단위 |
| notation_pref  | VARCHAR    | DEFAULT 'standard'  | 숫자 표기법 설정 |
| contact        | VARCHAR    |                     | 연락처(선택) |
| last_login     | TIMESTAMP  |                     | 마지막 로그인 시간 |
| created_at     | TIMESTAMP  | DEFAULT now()       | 생성 시각 |
| updated_at     | TIMESTAMP  | DEFAULT now()       | 수정 시각 |

---

## 2. USER_BACKUPS

| 컬럼명         | 타입        | 제약조건        | 설명 |
|----------------|------------|-----------------|------|
| id             | BIGSERIAL  | PK              | 백업 요청 ID |
| user_id        | BIGINT     | FK → users.id   | 요청자 |
| type           | VARCHAR    | NOT NULL        | 백업 종류 (model, dataset, showcase) |
| file_path      | VARCHAR    |                 | 결과 파일 경로 |
| status         | VARCHAR    |                 | 상태 (pending, completed, failed) |
| requested_at   | TIMESTAMP  | DEFAULT now()   | 요청 시각 |
| completed_at   | TIMESTAMP  |                 | 완료 시각 |

---

## 3. TEAMS

| 컬럼명         | 타입        | 제약조건        | 설명 |
|----------------|------------|-----------------|------|
| id             | BIGSERIAL  | PK              | 팀 ID |
| name           | VARCHAR    | UNIQUE, NOT NULL| 팀 이름 |
| description    | TEXT       |                 | 설명 |
| owner_id       | BIGINT     | FK → users.id   | 팀 소유자 |
| credit_balance | INT        | DEFAULT 0       | 팀 크레딧 잔액 |
| created_at     | TIMESTAMP  | DEFAULT now()   | 생성 시각 |
| updated_at     | TIMESTAMP  | DEFAULT now()   | 수정 시각 |

---

## 4. TEAM_MEMBERS

| 컬럼명         | 타입        | 제약조건        | 설명 |
|----------------|------------|-----------------|------|
| id             | BIGSERIAL  | PK              | 멤버 ID |
| team_id        | BIGINT     | FK → teams.id   | 소속 팀 |
| user_id        | BIGINT     | FK → users.id   | 사용자 |
| role           | VARCHAR    | NOT NULL        | 역할 (Owner, Admin, Contributor, Viewer) |
| joined_at      | TIMESTAMP  | DEFAULT now()   | 가입 시각 |
| last_active    | TIMESTAMP  |                 | 최근 활동 시각 |

---

## 5. ROLES

| 컬럼명         | 타입        | 제약조건        | 설명 |
|----------------|------------|-----------------|------|
| id             | BIGSERIAL  | PK              | Role ID |
| name           | VARCHAR    | UNIQUE, NOT NULL| 역할명 (Owner, Admin, Contributor, Viewer, Guest) |
| description    | TEXT       |                 | 설명 |

---

## 6. USER_CREDITS

| 컬럼명         | 타입        | 제약조건        | 설명 |
|----------------|------------|-----------------|------|
| id             | BIGSERIAL  | PK              | ID |
| user_id        | BIGINT     | FK → users.id   | 사용자 |
| balance        | INT        | DEFAULT 0       | 현재 잔액 |
| total_earned   | INT        | DEFAULT 0       | 누적 획득 |
| total_spent    | INT        | DEFAULT 0       | 누적 사용 |
| updated_at     | TIMESTAMP  | DEFAULT now()   | 갱신 시각 |

---

## 7. CREDIT_TRANSACTIONS

| 컬럼명         | 타입        | 제약조건        | 설명 |
|----------------|------------|-----------------|------|
| id             | BIGSERIAL  | PK              | 트랜잭션 ID |
| user_id        | BIGINT     | FK → users.id   | 관련 사용자 |
| team_id        | BIGINT     | FK → teams.id   | 관련 팀 (nullable) |
| amount         | INT        | NOT NULL        | 금액 (+/-) |
| type           | VARCHAR    | NOT NULL        | earn, spend, admin_adjust |
| source         | VARCHAR    |                 | 발생 원인 (model_run, dataset_upload 등) |
| created_at     | TIMESTAMP  | DEFAULT now()   | 생성 시각 |

---

## 8. API_KEYS

| 컬럼명         | 타입        | 제약조건        | 설명 |
|----------------|------------|-----------------|------|
| id             | BIGSERIAL  | PK              | 키 ID |
| user_id        | BIGINT     | FK → users.id   | 발급자 |
| team_id        | BIGINT     | FK → teams.id   | 소속 팀 (nullable) |
| key            | VARCHAR    | UNIQUE, NOT NULL| API Key |
| scope          | VARCHAR    | NOT NULL        | 사용 범위 (model, dataset, both) |
| active         | BOOLEAN    | DEFAULT true    | 활성 여부 |
| created_at     | TIMESTAMP  | DEFAULT now()   | 발급 시각 |
| expired_at     | TIMESTAMP  |                 | 만료 시각 |

---

# 🔗 관계 개요

- `users` ↔ `teams` : N:M (via `team_members`)
- `users` ↔ `roles` : N:1 (via `team_members.role`)
- `users` ↔ `user_credits` : 1:1
- `users` ↔ `credit_transactions` : 1:N
- `teams` ↔ `credit_transactions` : 1:N
- `users` ↔ `user_backups` : 1:N
- `users` ↔ `api_keys` : 1:N
- `teams` ↔ `api_keys` : 1:N
