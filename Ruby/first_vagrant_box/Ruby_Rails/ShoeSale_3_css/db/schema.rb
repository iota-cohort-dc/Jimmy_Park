ActiveRecord::Schema.define(version: 20170527163013) do

  create_table "products", force: :cascade do |t|
    t.string   "name"
    t.integer  "amount"
    t.integer  "user_id"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  add_index "products", ["user_id"], name: "index_products_on_user_id"

  create_table "purchases", force: :cascade do |t|
    t.integer  "user_id"
    t.integer  "product_id"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  add_index "purchases", ["product_id"], name: "index_purchases_on_product_id"
  add_index "purchases", ["user_id"], name: "index_purchases_on_user_id"

  create_table "sells", force: :cascade do |t|
    t.integer  "user_id"
    t.integer  "product_id"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  add_index "sells", ["product_id"], name: "index_sells_on_product_id"
  add_index "sells", ["user_id"], name: "index_sells_on_user_id"

  create_table "users", force: :cascade do |t|
    t.string   "first_name"
    t.string   "last_name"
    t.string   "email"
    t.string   "password_digest"
    t.integer  "product_id"
    t.datetime "created_at",      null: false
    t.datetime "updated_at",      null: false
  end

  add_index "users", ["product_id"], name: "index_users_on_product_id"

end
