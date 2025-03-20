#include <stdio.h>
#include <string.h>

const char* classify_club(const char* description) {
    int hack = 0, algo = 0, game = 0, ai = 0, wine = 0, app = 0;

    // 키워드 검색
    if (strstr(description, "해킹") || strstr(description, "보안")) hack++;
    if (strstr(description, "알고리즘") || strstr(description, "코테")) algo++;
    if (strstr(description, "게임") || strstr(description, "유니티")) game++;
    if (strstr(description, "AI") || strstr(description, "GPT")) ai++;
    if (strstr(description, "프론트") || strstr(description, "백")) wine++;
    if (strstr(description, "플러터") || strstr(description, "앱")) app++;

    // 가장 많이 언급된 동아리 분류
    if (hack >= algo && hack >= game && hack >= ai && hack >= wine && hack >= app) return "해킹동아리";
    if (algo >= hack && algo >= game && algo >= ai && algo >= wine && algo >= app) return "알고리즘동아리";
    if (game >= hack && game >= algo && game >= ai && game >= wine && game >= app) return "게임잼동아리";
    if (ai >= hack && ai >= algo && ai >= game && ai >= wine && ai >= app) return "AI고라동아리";
    if (wine >= hack && wine >= algo && wine >= game && wine >= ai && wine >= app) return "와인동아리";
    if (app >= hack && app >= algo && app >= game && app >= ai && app >= wine) return "앱솔루트동아리";

    return "미분류";
}

int main() {
    int n;
    char name[4], description[81];

    scanf("%d", &n);
    getchar();

    for (int i = 0; i < n; i++) {
        scanf("%[^:]: %[^]", name, description);
        getchar();

        const char* club = classify_club(description);
        printf("%s 대표는 %s.\n", club, name);
    }

    return 0;
}
