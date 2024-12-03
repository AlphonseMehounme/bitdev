pub const GOOD_WEIGHT: f32 = 1.0;
pub const BAD_WEIGHT: f32 = 2.0;

pub fn is_nice(good_deeds: u32, bad_deeds: u32) -> bool {
    let good_deeds = good_deeds as f32;
    let bad_deeds = bad_deeds as f32;

    if good_deeds == 0 && bad_deeds == 0 {
        return false;
    }
    let ratio = good_deeds / ((good_deeds * GOOD_WEIGHT) + (bad_deeds * BAD_WEIGHT));
    if ratio >= 0.75 {
        return true;
    } else {
        return false;
    }
}
