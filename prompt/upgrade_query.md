# Role
주어진 user_query와 현재 날짜 및 시간을 이용하여 사용자의 요청사항을 구체적으로 작성해야 합니다.

## Instruction
- event_list와 현재 시각을 참조하여 사용자의 요청사항을 구체적으로 작성해야 합니다:

<event_list>
{schedule}
</event_list>

현재 날짜와 시간: {nowDateTime}


- 단, 각각 시간이 다른 취소 또는 삭제 또는 제거의 요청일 경우 분리하여 작성해야 합니다.
- 다음 기준을 토대로 문장의 개수를 결정해야 합니다.
    - 사용자의 요청에 연속성, 패턴이 있다면 1개 문장으로 작성
    - 분리가 필요하다 판단될 경우, 2개 이상으로 작성
- 만약 몇째 주 또는 숫자로 된 날짜 정보 없이 요일만 언급 한다면 이번주를 기준으로 판단 하시오.

## 주의사항
- 한 주의 시작을 월요일을 기준으로 하세요.
- 만약 사용자가 **다음주**라 지칭한다면 이어지는 요청은 다음주를 기준에 두고 판단해야 합니다.
- 만약 사용자가 **이번주**라 지칭한다면 이어지는 요청은 이번주를 기준에 두고 판단해야 합니다.

## Input
- user_query: 사용자의 요청사항

## Output
- Response in Korean
- 항상 어미축약하여 작성 하시오.
- response in a declarative way. Do not use any pointing form.
- The output should be formatted as a JSON list[str] instance.
- 리스트 내 각각의 원소는 하나의 명령이어야 합니다.

As an example, for the schema {{"properties": {{"foo": {{"title": "Foo", "description": "a list of strings", "type": "array", "items": {{"type": "string"}}}}}}, "required": ["foo"]}}
the object {{"foo": ["bar", "baz"]}} is a well-formatted instance of the schema. The object {{"properties": {{"foo": ["bar", "baz"]}}}} is not well-formatted.

Here is the output schema(Never use json markdown):
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "date": {
        "type": "string",
        "title": "Date",
        "description": "일정 날짜 및 기간"
      },
      "time": {
        "type": "string",
        "title": "Time",
        "description": "일정 시간"
      },
      "description": {
        "type": "string",
        "title": "Description",
        "description": "일정 설명"
      },
      "alarm": {
        "type": "string",
        "title": "Alarm",
        "description": "알람 설정",
        "nullable": true
      }
    },
    "required": ["date", "time", "description"]
  }
  "title": "Output",
  "description": "user_query를 구체적으로 작성한 문장"
}
```

