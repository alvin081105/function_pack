#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>
#include <algorithm>
using namespace std;

struct Skill {
    string name;
    string energyType;
    int energyCost;
    int power;
};

int main() {
    int n, m;
    cin >> n >> m;

    vector<Skill> skills(n);
    unordered_map<string, int> energyPool;

    for (int i = 0; i < n; ++i) {
        cin >> skills[i].name >> skills[i].energyType >> skills[i].energyCost >> skills[i].power;
    }

    vector<string> addedEnergies(m);
    for (int i = 0; i < m; ++i) {
        cin >> addedEnergies[i];
    }

    for (const string& energy : addedEnergies) {
        energyPool[energy]++;

        Skill* bestSkill = nullptr;

        for (Skill& skill : skills) {
            if (energyPool[skill.energyType] >= skill.energyCost) {
                if (!bestSkill ||
                    skill.power > bestSkill->power ||
                    (skill.power == bestSkill->power && skill.energyCost < bestSkill->energyCost)) {
                    bestSkill = &skill;
                }
            }
        }

        if (bestSkill) {
            cout << bestSkill->name << " " << bestSkill->power << endl;
        }
    }

    return 0;
}
