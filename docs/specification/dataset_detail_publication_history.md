# Dataset Detail – Publication History Specification

## 1. Screen Name

**Dataset Detail – Publication History (Zenodo DOIs)**

---

## 2. Purpose

* 해당 데이터셋이 \*\*Zenodo에 업로드된 이력(DOI 발급 포함)\*\*을 한눈에 확인할 수 있는 화면
* 연구자가 모델/데이터셋을 출판하고 인용할 수 있도록 관리
* 팀/개인 업로드 내역 구분, 각 버전과 연결된 DOI 기록 제공

---

## 3. Layout

### A. Header

* **Title**: `Publication History`
* **Breadcrumb**: `Datasets > Dataset Detail > Publication History`

### B. Main Content

1. **Publication List (Table View)**

   | Column         | Description                           |
   | -------------- | ------------------------------------- |
   | Version        | 데이터셋 버전 번호 (v1, v2 …)                 |
   | DOI            | Zenodo DOI 링크 (`https://doi.org/...`) |
   | Title          | Zenodo에 등록된 제목                        |
   | Authors        | 등록된 작성자 목록                            |
   | Date Published | Zenodo 업로드/수정 날짜                      |
   | Files          | 업로드된 파일 리스트(확장자, 크기 표시)               |
   | Notes          | 연구자 메모 (선택 입력 가능)                     |

2. **Detail Drawer / Modal (행 클릭 시)**

   * DOI 메타데이터 상세 정보(JSON → human-readable)
   * Citation formats (BibTeX, APA, MLA 등)
   * Zenodo 원본 페이지 링크

3. **Actions**

   * \[Publish to Zenodo] 버튼

     * OAuth 인증 후 Zenodo 업로드 지원
   * \[Export Citation] 버튼

     * Citation 텍스트 복사/다운로드
   * \[Refresh Metadata] 버튼

     * Zenodo API 호출하여 DOI 정보 최신화

### C. Sidebar

* Linked Dataset Info (간단 요약: name, description, owner)
* Navigation to other Dataset Detail tabs (Overview, Schema, Versions, Usage …)

---

## 4. States

* **Empty State**:

  * `"No publication history found for this dataset."`
  * \[Publish to Zenodo] 버튼 강조
* **Loading State**: 스피너와 `"Fetching Zenodo records..."` 표시
* **Error State**:

  * Zenodo API 오류 시: `"Failed to fetch publication data. Retry later."`

---

## 5. Permissions

* **Viewer**: Publication 기록 열람만 가능
* **Editor/Owner**: Zenodo 업로드, 메타데이터 동기화, 메모 추가 가능
* **Admin**: DOI 삭제(로컬 기록만 삭제, Zenodo 원본은 유지)

---

## 6. API Integration

* **Zenodo REST API**

  * `GET /records/{doi}` : DOI 메타데이터 조회
  * `POST /deposit/depositions` : 신규 업로드
  * `PUT /deposit/depositions/{id}` : 업데이트

* **Local DB**

  * `publication_history` 테이블: dataset\_id, version, doi, metadata, memo 저장

---

## 7. Example Wireframe (텍스트)

```
-------------------------------------------------
Dataset: Climate Time Series (v3)

[ Publication History ]

+---------+---------------------+----------------+------------------+-------------+--------+
| Version | DOI                 | Title          | Authors          | Published   | Files  |
+---------+---------------------+----------------+------------------+-------------+--------+
| v3      | doi:10.5281/zenodo...| Climate Data v3| Yoon, J.; Kim, S.| 2025-08-10  | 3 files|
| v2      | doi:10.5281/zenodo...| Climate Data v2| Yoon, J.         | 2025-07-01  | 2 files|
+---------+---------------------+----------------+------------------+-------------+--------+

[ Publish to Zenodo ] [ Export Citation ] [ Refresh Metadata ]
-------------------------------------------------
```
